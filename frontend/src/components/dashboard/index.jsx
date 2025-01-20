import * as React from 'react';
import PropTypes from 'prop-types';
import { Outlet } from 'react-router-dom';
import { extendTheme, styled } from '@mui/material/styles';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import StoreIcon from '@mui/icons-material/Store';
import PeopleIcon from '@mui/icons-material/People';
import BarChartIcon from '@mui/icons-material/BarChart';
import Grid from '@mui/material/Grid2';
import CloudCircleIcon from '@mui/icons-material/CloudCircle';
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout,ThemeSwitcher } from '@toolpad/core/DashboardLayout';
import { PageContainer } from '@toolpad/core/PageContainer';
import { useNavigate, useLocation } from 'react-router-dom';
import shoppingBagLogoDesign from '../../assets/shopping-bag-logo-design.jpg';
import { CardMedia,Stack,Typography,Chip,Tooltip,IconButton,TextField     } from '@mui/material';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import SearchIcon from '@mui/icons-material/Search';
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

function ToolbarActionsSearch() {
  return (
    <Stack direction="row">
      <Tooltip title="Search" enterDelay={1000}>
        <div>
          <IconButton
            type="button"
            aria-label="search"
            sx={{
              display: { xs: 'inline', md: 'none' },
            }}
          >
            <SearchIcon />
          </IconButton>
        </div>
      </Tooltip>
      <TextField
        label="Search"
        variant="outlined"
        size="small"
        slotProps={{
          input: {
            endAdornment: (
              <IconButton type="button" aria-label="search" size="small">
                <SearchIcon />
              </IconButton>
            ),
            sx: { pr: 0.5 },
          },
        }}
        sx={{ display: { xs: 'none', md: 'inline-block' }, mr: 1 }}
      />
      <ThemeSwitcher />
    </Stack>
  );
}

function SidebarFooter({ mini }) {
  return (
    <Typography
      variant="caption"
      sx={{ m: 1, whiteSpace: 'nowrap', overflow: 'hidden' }}
    >
      {mini ? '© MUI' : `© ${new Date().getFullYear()} Made with love by MUI`}
    </Typography>
  );
}

SidebarFooter.propTypes = {
  mini: PropTypes.bool.isRequired,
};

function CustomAppTitle() {
  return (
    <Stack direction="row" alignItems="center" spacing={2}>
      <CloudCircleIcon fontSize="large" color="primary" />
      <Typography variant="h6">My App</Typography>
      <Chip size="small" label="BETA" color="info" />
      <Tooltip title="Connected to production">
        <CheckCircleIcon color="success" fontSize="small" />
      </Tooltip>
    </Stack>
  );
}



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
      branding={{
        logo: <CardMedia  component="img"
        image={shoppingBagLogoDesign} alt="Shoping logo" />,
        title: 'Shopping',
      }}
      router={{
        navigate: (path) => navigate(path),
        pathname: location.pathname,
        searchParams: new URLSearchParams(location.search),
      }}
      theme={demoTheme}
      window={demoWindow}
    >
      <DashboardLayout  slots={{
          appTitle: CustomAppTitle,
          toolbarActions: ToolbarActionsSearch,
          sidebarFooter: SidebarFooter,
        }}>
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


