import streamlit as st

st.set_page_config(layout="wide")

# Add SEO meta tags via custom HTML
st.markdown(
    """
<meta name="description" content="Find monthly rentals in Chiang Mai, Thailand. Interactive map showing available apartments and condos with pricing, availability, and detailed information. Updated regularly.">
<meta name="keywords" content="Chiang Mai rentals, monthly rentals Chiang Mai, apartments Chiang Mai, condos Chiang Mai, Thailand rentals, Chiang Mai accommodation, long-term rentals Thailand">
<meta name="author" content="CM Rentals">
<meta property="og:title" content="Chiang Mai Monthly Rentals - Find Your Perfect Apartment">
<meta property="og:description" content="Interactive map of monthly rentals in Chiang Mai, Thailand. Find apartments and condos with detailed pricing and availability information.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://cm-rentals.com">
<meta property="og:site_name" content="Chiang Mai Rentals">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Chiang Mai Monthly Rentals">
<meta name="twitter:description" content="Find monthly rentals in Chiang Mai with our interactive map. View pricing, availability, and property details.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://cm-rentals.com">
""",
    unsafe_allow_html=True,
)

# form_page = st.Page("pg/form.py", title="Property form", icon="🏠")
map_page = st.Page("pg/map.py", title="Chiang Mai rentals", icon="🏠")

# Create the navigation
# pg = st.navigation([form_page, map_page])
pg = st.navigation([map_page])

# Run the selected page
pg.run()
