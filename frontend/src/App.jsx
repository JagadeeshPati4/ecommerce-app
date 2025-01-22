import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

const ECommerceDashboard = lazy(() => import('./components/dashboard'));
const DefualtDashboard = lazy(() =>
  import('./components/dashboard/index').then((mod) => ({ default: mod.DefualtDashboard }))
);
const Products = lazy(() => import('./components/products'));
const SignIn = lazy(() => import('./components/sign-In'));
const SignUp = lazy(() => import('./components/sign-up'));

export default function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          {/* Routes outside the dashboard */}
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-up" element={<SignUp />} />
          
          {/* Routes inside the dashboard */}
          <Route path="/" element={<ECommerceDashboard />}>
            <Route index element={<DefualtDashboard />} />
            <Route path="products" element={<Products />} />
            {/* Add more dashboard-specific routes here */}
          </Route>

          {/* Catch-all for undefined routes */}
          <Route path="*" element={<div>Page Not Found</div>} />
        </Routes>
      </Suspense>
    </Router>
  );
}
