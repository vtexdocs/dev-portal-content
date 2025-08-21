# Retrieving ads

VTEX Ads allows you to retrieve sponsored products to display in your storefront. This guide explains how to use the API to fetch ads for different contexts and page types.

## API endpoint

Use the following endpoint to retrieve sponsored products:

```
GET https://{accountName}.vtexcommercestable.com.br/api/ads/sponsored-products
```

## Authentication

Include your VTEX API credentials in the request headers:

```javascript
headers: {
  'X-VTEX-API-AppKey': 'your-app-key',
  'X-VTEX-API-AppToken': 'your-app-token',
  'Content-Type': 'application/json'
}
```

## Query parameters

The API accepts the following query parameters:

- **`query`**: Search term or keyword
- **`category`**: Category ID to filter products
- **`context`**: Page context (e.g., `search`, `category`, `product_page`, `home`)
- **`limit`**: Number of products to return (default: 10, max: 50)
- **`page`**: Page number for pagination
- **`brand`**: Brand ID for brand-specific ads
- **`price_min`**: Minimum price filter
- **`price_max`**: Maximum price filter
- **`sort`**: Sorting criteria (relevance, price, popularity)

## Context-specific implementations

### Search results page

For search results pages, use the `search` context:

```javascript
const getSearchAds = async (searchTerm, page = 1) => {
  const params = {
    query: searchTerm,
    context: 'search',
    limit: 4,
    page: page
  };
  
  const queryParams = new URLSearchParams(params);
  
  const response = await fetch(
    `https://${accountName}.vtexcommercestable.com.br/api/ads/sponsored-products?${queryParams}`,
    {
      method: 'GET',
      headers: {
        'X-VTEX-API-AppKey': 'your-app-key',
        'X-VTEX-API-AppToken': 'your-app-token',
        'Content-Type': 'application/json'
      }
    }
  );
  
  return await response.json();
};

// Usage
const searchAds = await getSearchAds('smartphone');
```

### Category page

For category pages, use the `category` context:

```javascript
const getCategoryAds = async (categoryId) => {
  const params = {
    category: categoryId,
    context: 'category',
    limit: 6,
    sort: 'relevance'
  };
  
  const queryParams = new URLSearchParams(params);
  
  const response = await fetch(
    `https://${accountName}.vtexcommercestable.com.br/api/ads/sponsored-products?${queryParams}`,
    {
      method: 'GET',
      headers: {
        'X-VTEX-API-AppKey': 'your-app-key',
        'X-VTEX-API-AppToken': 'your-app-token',
        'Content-Type': 'application/json'
      }
    }
  );
  
  return await response.json();
};

// Usage
const categoryAds = await getCategoryAds('electronics');
```

### Product detail page

For product detail pages, use the `product_page` context to get relevant cross-sell and upsell recommendations:

```javascript
const getProductPageAds = async (productId, categoryId) => {
  const params = {
    category: categoryId,
    context: 'product_page',
    exclude: productId, // Exclude current product
    limit: 4,
    sort: 'relevance'
  };
  
  const queryParams = new URLSearchParams(params);
  
  const response = await fetch(
    `https://${accountName}.vtexcommercestable.com.br/api/ads/sponsored-products?${queryParams}`,
    {
      method: 'GET',
      headers: {
        'X-VTEX-API-AppKey': 'your-app-key',
        'X-VTEX-API-AppToken': 'your-app-token',
        'Content-Type': 'application/json'
      }
    }
  );
  
  return await response.json();
};

// Usage
const productPageAds = await getProductPageAds('product-123', 'electronics');
```

### Home page

For home page implementations, use the `home` context:

```javascript
const getHomePageAds = async () => {
  const params = {
    context: 'home',
    limit: 8,
    sort: 'popularity'
  };
  
  const queryParams = new URLSearchParams(params);
  
  const response = await fetch(
    `https://${accountName}.vtexcommercestable.com.br/api/ads/sponsored-products?${queryParams}`,
    {
      method: 'GET',
      headers: {
        'X-VTEX-API-AppKey': 'your-app-key',
        'X-VTEX-API-AppToken': 'your-app-token',
        'Content-Type': 'application/json'
      }
    }
  );
  
  return await response.json();
};

// Usage
const homePageAds = await getHomePageAds();
```

## Response structure

The API returns a structured response:

```javascript
{
  "products": [
    {
      "id": "product-123",
      "name": "Product Name",
      "brand": "Brand Name",
      "price": 99.99,
      "image": "https://example.com/image.jpg",
      "url": "https://store.com/product-123",
      "campaign": {
        "id": "campaign-456",
        "name": "Summer Sale",
        "bid_amount": 1.50
      },
      "tracking": {
        "impression_id": "imp-789",
        "click_url": "https://ads.vtex.com/click/...",
        "view_url": "https://ads.vtex.com/view/..."
      }
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 25,
    "has_next": true
  }
}
```

## Error handling

Implement robust error handling for your ad requests:

```javascript
const getSponsoredProductsSafely = async (params) => {
  try {
    const queryParams = new URLSearchParams(params);
    
    const response = await fetch(
      `https://${accountName}.vtexcommercestable.com.br/api/ads/sponsored-products?${queryParams}`,
      {
        method: 'GET',
        headers: {
          'X-VTEX-API-AppKey': 'your-app-key',
          'X-VTEX-API-AppToken': 'your-app-token',
          'Content-Type': 'application/json'
        }
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('VTEX Ads API Error:', error);
    
    // Return fallback structure
    return {
      products: [],
      pagination: {
        page: 1,
        limit: params.limit || 10,
        total: 0,
        has_next: false
      },
      error: error.message
    };
  }
};
```

## Best practices

1. **Use appropriate context**: Always specify the correct `context` parameter for your page type to ensure relevant ad targeting.

2. **Implement caching**: Cache responses for a few minutes to improve performance and reduce API calls.

3. **Handle errors gracefully**: Always implement fallback behavior when ads are not available.

4. **Track events**: Remember to track impressions and clicks after displaying ads.

5. **Respect rate limits**: Implement proper throttling to avoid hitting API rate limits.

## Next steps

After retrieving ads, make sure to:

1. [Track ad events](./ads-events.md) (impressions, clicks, views)
2. [Synchronize your catalog](./synchronizing-the-catalog-with-vtex-ads.md) to ensure accurate product information
3. Monitor performance and optimize based on metrics