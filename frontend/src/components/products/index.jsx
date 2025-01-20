import React, { useEffect, useState } from "react";
import axios from "axios";
import { Grid, Card, CardContent, CardMedia, Typography, Box, CircularProgress, Button, CardActionArea } from "@mui/material";

const ProductsPage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch products from API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("https://fakestoreapi.com/products");
        setProducts(response.data);
      } catch (error) {
        setError("Failed to load products.");
        console.error("Error fetching products:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <Typography variant="h6" color="error">{error}</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ flexGrow: 1, padding: 2 }}>
      <Grid container spacing={3} alignItems="stretch">
        {products.map((product) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={product.id}>
            <Card 
              sx={{
                height: '100%',
                boxShadow: '0 4px 12px rgba(0, 0, 0, 0.1)',
                borderRadius: '12px',
                transition: 'transform 0.3s, box-shadow 0.3s',
                '&:hover': {
                  transform: 'scale(1.03)',
                  boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
                },
              }}
            >
              <CardActionArea sx={{ flexGrow: 1 }}>
                <CardMedia
                  component="img"
                  image={product.image}
                  alt={product.title}
                  sx={{ height: 300,width:'100%', objectFit: "fill",display: "block"}}
                />
                <CardContent sx={{display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',}}>
                  <Typography 
                    variant="h6" 
                    gutterBottom 
                    sx={{ fontWeight: 'bold', fontSize: '1rem' }}
                  >
                    {product.title}
                  </Typography>
                  <Typography 
                    variant="body2" 
                    color="text.secondary" 
                    sx={{ marginBottom: 1 }}
                  >
                    {product.description.length > 30 ? 
                      `${product.description.substring(0, 30)}...` : 
                      product.description
                    }
                  </Typography>
                  
                </CardContent>
              </CardActionArea>
              <Box sx={{ padding: '16px' }}>
                <Typography 
                  variant="subtitle1" 
                  color="text.primary" 
                  sx={{ fontWeight: 'bold', fontSize: '1.1rem' }}
                >
                  ${product.price}
                </Typography>
              </Box>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>

  );
};

export default ProductsPage;
