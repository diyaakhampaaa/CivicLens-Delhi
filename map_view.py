
"""Interactive Delhi location picker for CivicLens.

Locality coordinates are approximate map references, not authoritative
administrative boundaries. No fabricated complaint pins are displayed.
"""

import folium
import streamlit as st
from streamlit_folium import st_folium


DELHI_CENTER = (28.6139, 77.2090)

# Approximate reference coordinates for map navigation only.
# These do not confirm municipal jurisdiction.
DELHI_LOCALITIES = {
    "Central Delhi (reference)": (28.6448, 77.2167),
    "Connaught Place (reference)": (28.6315, 77.2167),
    "Rohini (reference)": (28.7495, 77.0565),
    "Dwarka (reference)": (28.5921, 77.0460),
    "Saket (reference)": (28.5245, 77.2066),
    "Lajpat Nagar (reference)": (28.5677, 77.2433),
    "Karol Bagh (reference)": (28.6514, 77.1907),
    "Shahdara (reference)": (28.6733, 77.2890),
}


def render_delhi_map():
    """Render the Delhi map and return the selected location.

    Returns:
        A dictionary containing locality, latitude, longitude, and
        selection_method, or None if no location has been selected.
    """

    # Initialize session state before handling any selections.
    if "civiclens_selected_point" not in st.session_state:
        st.session_state["civiclens_selected_point"] = None

    if "_civiclens_last_locality" not in st.session_state:
        st.session_state["_civiclens_last_locality"] = "Choose a locality..."

    if "_civiclens_last_processed_click" not in st.session_state:
        st.session_state["_civiclens_last_processed_click"] = None

    st.subheader("Explore Delhi")
    st.caption(
        "Choose a reference locality or click the map. Coordinates are "
        "approximate and do not establish administrative jurisdiction."
    )

    locality_names = ["Choose a locality..."] + list(
        DELHI_LOCALITIES.keys()
    )

    selected_locality = st.selectbox(
        "Jump to a locality",
        locality_names,
        key="civiclens_map_locality",
    )

    # Update the selected point only when the dropdown actually changes.
    # This prevents an unchanged dropdown selection from repeatedly
    # overwriting a location chosen by clicking the map.
    locality_changed = (
        selected_locality
        != st.session_state["_civiclens_last_locality"]
    )

    if locality_changed:
        st.session_state["_civiclens_last_locality"] = selected_locality

        if selected_locality != "Choose a locality...":
            lat, lon = DELHI_LOCALITIES[selected_locality]

            st.session_state["civiclens_selected_point"] = {
                "locality": selected_locality.replace(" (reference)", ""),
                "latitude": float(lat),
                "longitude": float(lon),
                "selection_method": "locality_reference",
            }

    # Center the map on the selected dropdown locality, or on Delhi.
    if selected_locality != "Choose a locality...":
        default_lat, default_lon = DELHI_LOCALITIES[selected_locality]
        zoom_level = 12
    else:
        default_lat, default_lon = DELHI_CENTER
        zoom_level = 10

    map_object = folium.Map(
        location=[default_lat, default_lon],
        zoom_start=zoom_level,
        tiles="OpenStreetMap",
        control_scale=True,
    )

    # General Delhi reference point, not a complaint or jurisdiction pin.
    folium.Marker(
        location=DELHI_CENTER,
        tooltip="Delhi map reference",
        popup=(
            "Delhi reference point. This is not a complaint location "
            "or an administrative boundary."
        ),
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(map_object)

    # Display approximate locality reference points.
    for name, (lat, lon) in DELHI_LOCALITIES.items():
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            color="#0F766E",
            fill=True,
            fill_opacity=0.75,
            tooltip=name,
            popup=f"{name} — approximate reference point only",
        ).add_to(map_object)

    # Highlight the currently selected dropdown locality.
    if selected_locality != "Choose a locality...":
        folium.Marker(
            location=[default_lat, default_lon],
            tooltip="Selected reference locality",
            popup=selected_locality,
            icon=folium.Icon(color="green"),
        ).add_to(map_object)

    # Display the currently selected user point, if available.
    existing_point = st.session_state["civiclens_selected_point"]

    if existing_point:
        folium.Marker(
            location=[
                existing_point["latitude"],
                existing_point["longitude"],
            ],
            tooltip="Your selected point",
            popup="User-selected location; jurisdiction not verified",
            icon=folium.Icon(color="red"),
        ).add_to(map_object)

    # Return map clicks to Streamlit.
    map_state = st_folium(
        map_object,
        height=470,
        use_container_width=True,
        returned_objects=["last_clicked"],
        key="civiclens_delhi_map",
    )

    clicked = map_state.get("last_clicked") if map_state else None

    if clicked and "lat" in clicked and "lng" in clicked:
        click_point = (
            round(float(clicked["lat"]), 6),
            round(float(clicked["lng"]), 6),
        )

        # Process a click only once, so ordinary Streamlit reruns do not
        # continually reset the selected point.
        if (
            click_point
            != st.session_state["_civiclens_last_processed_click"]
        ):
            st.session_state["_civiclens_last_processed_click"] = (
                click_point
            )

            st.session_state["civiclens_selected_point"] = {
                "locality": "Map-selected point",
                "latitude": click_point[0],
                "longitude": click_point[1],
                "selection_method": "map_click",
            }

    point = st.session_state["civiclens_selected_point"]

    if point:
        st.success("Location selected")

        col1, col2 = st.columns(2)

        col1.metric("Latitude", f'{point["latitude"]:.5f}')
        col2.metric("Longitude", f'{point["longitude"]:.5f}')

        st.caption(
            "This is a selected map location, not confirmation of the "
            "responsible authority or a verified civic incident."
        )

    return point
