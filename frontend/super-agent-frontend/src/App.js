// This file is the main entry point and router for the application. It decides which page to show based on the user's authentication state.
// Este archivo es el punto de entrada principal y enrutador de la aplicación. Decide qué página mostrar según el estado de autenticación del usuario.

import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AuthPage from './pages/AuthPage';
import HomePage from './pages/HomePage';
import './App.css';

// Simulated authentication state. Replace with real auth logic (e.g., JWT, context, etc.).
// Estado de autenticación simulado. Reemplaza con lógica real de autenticación (por ejemplo, JWT, context, etc.).
const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Handler to simulate login (should be replaced with real logic).
  // Manejador para simular inicio de sesión (debe ser reemplazado por lógica real).
  const handleLogin = () => setIsAuthenticated(true);

  // Handler to simulate logout (should be replaced with real logic).
  // Manejador para simular cierre de sesión (debe ser reemplazado por lógica real).
  const handleLogout = () => setIsAuthenticated(false);

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Super Agent</h1>
        </header>
        <Routes>
          {/*If not authenticated, show AuthPage. */}
          {/*Si no está autenticado, mostrar AuthPage. */}
          <Route path="/auth" element={<AuthPage onLogin={handleLogin} />} />
          {/*If authenticated, show HomePage. */}
          {/*Si está autenticado, mostrar HomePage. */}
          <Route path="/home" element={<HomePage onLogout={handleLogout} />} />
          {/*Redirect based on authentication state. */}
          {/*Redirigir según el estado de autenticación. */}
          <Route path="*" element={isAuthenticated ? <Navigate to="/home" /> : <Navigate to="/auth" />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;