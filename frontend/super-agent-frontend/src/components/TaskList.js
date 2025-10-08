// This component is responsible for displaying the list of tasks and the filtering options.
// Este componente se encarga de mostrar la lista de tareas y las opciones de filtrado.

import React from 'react';
import TaskItem from './TaskItem';

// The TaskList component receives the list of tasks and filter handlers as props.
// El componente TaskList recibe la lista de tareas y los manejadores de filtro como props.


const TaskList = ({ tasks, onTaskClick, filters, onFilterChange, subjects = [], statuses = [], types = [] }) => {
	return (
		<div>
			{/* Filters section */}
			{/* Sección de filtros */}
			<div style={{ marginBottom: '20px', display: 'flex', gap: '20px' }}>
				{/* Subject filter */}
				{/* Filtro por materia */}
				<select name="subject" value={filters.subject} onChange={onFilterChange}>
					<option value="">All Subjects</option>
					{subjects.map(subject => (
						<option key={subject} value={subject}>{subject}</option>
					))}
				</select>
				{/* Status filter */}
				{/* Filtro por estado */}
				<select name="status" value={filters.status} onChange={onFilterChange}>
					<option value="">All Status</option>
					{statuses.map(status => (
						<option key={status} value={status}>{status}</option>
					))}
				</select>
				{/* Task type filter */}
				{/* Filtro por tipo de tarea */}
				<select name="task_type" value={filters.task_type} onChange={onFilterChange}>
					<option value="">All Types</option>
					{types.map(type => (
						<option key={type} value={type}>{type}</option>
					))}
				</select>
			</div>

			{/* Tasks list */}
			{/* Lista de tareas */}
			<div>
				{tasks.length === 0 ? (
					<p>No tasks found</p>
				) : (
					tasks.map((task) => (
						<TaskItem key={task.id} task={task} onClick={() => onTaskClick(task)} />
					))
				)}
			</div>
		</div>
	);
};

export default TaskList;
