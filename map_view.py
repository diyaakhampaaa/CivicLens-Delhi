"""Optional interactive Delhi location picker for Streamlit."""

import streamlit as st

def render_delhi_map():
    """Render a simple Folium map if dependencies are installed.

    Returns a dict with latitude/longitude and an optional locality label, or None
    when no map point has been selected. Manual locality entry remains available.
    """
    try:
        import folium
        from streamlit_folium import st_folium
    except ImportError:
        st.info("Map feature needs folium and streamlit-folium. Enter your locality manually below.")
        return None

    default_lat = 28.6139
    default_lon = 77.2090
    m = folium.Map(location=[default_lat, default_lon], zoom_start=11, control_scale=True)
    folium.Marker(
        [default_lat, default_lon],
        tooltip="New Delhi",
        popup="New Delhi — move/zoom and click a point to select coordinates",
        icon=folium.Icon(color="orange", icon="info-sign"),
    ).add_to(m)
    result = st_folium(
        m,
        height=330,
        use_container_width=True,
        returned_objects=["last_clicked"],
        key="civiclens_delhi_map",
    )
    clicked = (result or {}).get("last_clicked")
    if not clicked:
        return None
    lat = clicked.get("lat")
    lon = clicked.get("lng")
    if lat is None or lon is None:
        return None
    return {
        "latitude": round(float(lat), 6),
        "longitude": round(float(lon), 6),
        "locality": "Map-selected point",
        "landmark": "",
    }
