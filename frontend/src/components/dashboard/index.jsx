import * as React from 'react';
import { Outlet } from 'react-router-dom';
import { extendTheme, styled } from '@mui/material/styles';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import StoreIcon from '@mui/icons-material/Store';
import PeopleIcon from '@mui/icons-material/People';
import BarChartIcon from '@mui/icons-material/BarChart';
import Grid from '@mui/material/Grid2';
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { PageContainer } from '@toolpad/core/PageContainer';
import { useNavigate, useLocation } from 'react-router-dom';
import { Box } from '@mui/material';

// Navigation Configuration
const NAVIGATION = [
  { kind: 'header', title: 'Shop Management' },
  {
    segment: 'Products',
    title: 'Products',
    icon: <StoreIcon />,
    link: '/Products', // Matches path in Routes
  },
  {
    segment: 'orders',
    title: 'Orders',
    icon: <ShoppingCartIcon />,
    link: '/orders', // Added link
  },
  { kind: 'divider' },
  { kind: 'header', title: 'Analytics' },
  {
    segment: 'analytics',
    title: 'Sales Analytics',
    icon: <BarChartIcon />,
    link: '/analytics', // Added link
  },
  { kind: 'header', title: 'Customer Management' },
  {
    segment: 'customers',
    title: 'Customers',
    icon: <PeopleIcon />,
    link: '/customers', // Added link
  },
];


// Custom Theme
const demoTheme = extendTheme({
  colorSchemes: { light: true, dark: true },
  colorSchemeSelector: 'class',
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 900,
      lg: 1200,
      xl: 1536,
    },
  },
});




// Skeleton Component
const Skeleton = styled('div')(({ theme, height }) => ({
  backgroundColor: theme.palette.action.hover,
  borderRadius: theme.shape.borderRadius,
  height,
  content: '" "',
}));

export default function ECommerceDashboard(props) {
  const { window } = props;
  const navigate = useNavigate();
  const location = useLocation();
  // const router = useDemoRouter('/');

  // Mock window for demo purposes
  const demoWindow = window ? window() : undefined;

  return (
    <AppProvider
      navigation={NAVIGATION}
      router={{
        navigate: (path) => navigate(path),
        pathname: location.pathname,
        searchParams: new URLSearchParams(location.search),
      }}
      theme={demoTheme}
      window={demoWindow}
    >
      <DashboardLayout >
        <PageContainer  sx={{scrollbarWidth: "none"}}>
          <Outlet />
        </PageContainer>
      </DashboardLayout>
    </AppProvider>
  );
}


export const DefualtDashboard= () =>{
  return (
    <>
     <Grid container spacing={2}>
            <Grid size={12}>
              <h1>Welcome to the E-Commerce Dashboard</h1>
            </Grid>
            <Grid size={6}>
              <h2>Quick Stats</h2>
              <Skeleton height={150} />
            </Grid>
            <Grid size={6}>
              <h2>Recent Orders</h2>
              <Skeleton height={150} />
            </Grid>
            <Grid size={12}>
              <h2>Top Selling Products</h2>
              <Skeleton height={300} />
            </Grid>
            <Grid size={4}>
              <h2>New Customers</h2>
              <Skeleton height={200} />
            </Grid>
            <Grid size={8}>
              <h2>Sales Overview</h2>
              <Skeleton height={300} />
            </Grid>
          </Grid>
    </>
  )
}


