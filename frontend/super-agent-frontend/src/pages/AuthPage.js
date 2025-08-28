// This page is responsible for displaying both the Login and Register forms when the user is not authenticated.
// It is the entry point for new or unauthenticated users.
// Esta página se encarga de mostrar ambos formularios, el de inicio de sesión y el de registro, cuando el usuario no está autenticado.
// Es el punto de entrada para usuarios nuevos o no autenticados.

import React from 'react';
import LoginForm from '../components/LoginForm';
import RegisterForm from '../components/RegisterForm';

// The AuthPage component renders the login and register forms side by side or stacked.
// El componente AuthPage renderiza los formularios de inicio de sesión y registro, uno al lado del otro o apilados.

const AuthPage = ({ onLogin }) => {
	return (
		<div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '40px', padding: '40px' }}>
			{/* Login form for existing users. */}
			{/* Formulario de inicio de sesión para usuarios existentes. */}
			<LoginForm onLogin={onLogin} />
			{/* Register form for new users. */}
			{/* Formulario de registro para nuevos usuarios. */}
			<RegisterForm />
		</div>
	);
};

export default AuthPage;
