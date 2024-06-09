def recommend_hotels(df, price_range, district, amenities):
    filtered_df = df
    
    # Check if price_range can be split into exactly two parts
    if '-' not in price_range or len(price_range.split('-')) != 2:
        raise ValueError(f"Invalid price range: {price_range}. Expected format is 'min-max'.")

    min_price, max_price = map(int, price_range.split('-'))
    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
        filtered_df = filtered_df[(filtered_df['Room Rates'] >= min_price) & (filtered_df['Room Rates'] <= max_price)]
    
    if district:
        filtered_df = filtered_df[filtered_df['District'].str.contains(district, case=False)]
    
    if amenities:
        for amenity in amenities:
            filtered_df = filtered_df[filtered_df['Amenities'].str.contains(amenity.strip(), case=False)]
    
    return filtered_df