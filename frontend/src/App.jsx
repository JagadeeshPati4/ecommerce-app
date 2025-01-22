import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ECommerceDashboard, { DefualtDashboard } from './components/dashboard/index';
import Products from './components/products/index';
import SignIn from './components/sign-In/index';
import SignUp from './components/sign-up/index';
// import Orders from './pages/Orders';
// import Analytics from './pages/Analytics';
// import Customers from './pages/Customers';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ECommerceDashboard />}>
          <Route index element={<DefualtDashboard />} />
          <Route path="Products" element={<Products />} />
          <Route path="/Sign-in" element={<SignIn />} />
          <Route path="/Sign-up" element={<SignUp />} />
          {/* <Route path="orders" element={<Orders />} />
          <Route path="analytics" element={<Analytics />} />
          <Route path="customers" element={<Customers />} /> */}
        </Route>
      </Routes>
    </Router>
  );
}
