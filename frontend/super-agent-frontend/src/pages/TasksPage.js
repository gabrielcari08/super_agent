// This page is responsible for displaying the main options for tasks: add a new task or view the list of tasks.
// Esta página se encarga de mostrar las opciones principales para tareas: añadir una nueva tarea o ver la lista de tareas.

import React from 'react';
import { useNavigate } from 'react-router-dom';

// The TasksPage component renders two buttons: Add Task and View Tasks.
// El componente TasksPage renderiza dos botones: Añadir Tarea y Ver Tareas.

const TasksPage = () => {
	const navigate = useNavigate();

	// Handler for Add Task button
	// Manejador para el botón Añadir Tarea
	const handleAddTask = () => {
		navigate('/tasks/add');
	};

	// Handler for View Tasks button
	// Manejador para el botón Ver Tareas
	const handleViewTasks = () => {
		navigate('/tasks/list');
	};

	return (
		<div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '40px', gap: '30px' }}>
			<h2>Tasks / Tareas</h2>
			<div style={{ display: 'flex', gap: '20px' }}>
				<button onClick={handleAddTask} style={{ padding: '12px 24px', fontSize: '16px' }}>Add Task / Añadir Tarea</button>
				<button onClick={handleViewTasks} style={{ padding: '12px 24px', fontSize: '16px' }}>View Tasks / Ver Tareas</button>
			</div>
		</div>
	);
};

export default TasksPage;
