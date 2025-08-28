// This page is responsible for displaying the main content after the user logs in.
// It welcomes the user and shows the main options of the app (add task, add expense, etc.).
// Esta página se encarga de mostrar el contenido principal después de que el usuario inicia sesión.
// Da la bienvenida al usuario y muestra las opciones principales de la app (añadir tarea, añadir gasto, etc.).

import React from 'react';

// The HomePage component renders the welcome message and main options.
// El componente HomePage renderiza el mensaje de bienvenida y las opciones principales.

const HomePage = () => {
	return (
		<div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '40px' }}>
			{/* Welcome message */}
			{/* Mensaje de bienvenida */}
			<h1>Welcome to Super-Agent!</h1>
			{/* Main options (add task, add expense, etc.) */}
			{/* Opciones principales (añadir tarea, añadir gasto, etc.) */}
			<div style={{ marginTop: '30px', display: 'flex', gap: '20px' }}>
				<button style={{ padding: '12px 24px', fontSize: '16px' }}>Tasks</button>
				<button style={{ padding: '12px 24px', fontSize: '16px' }}>Expenses</button>
				{/* You can add more options here / Puedes agregar más opciones aquí */}
			</div>
		</div>
	);
};

export default HomePage;
