// This component is responsible for displaying a single task in the list.
// Este componente se encarga de mostrar una sola tarea en la lista.

import React from 'react';

// The TaskItem component receives a task and a click handler as props.
// El componente TaskItem recibe una tarea y un manejador de click como props.


const TaskItem = ({ task, onClick }) => {
	return (
		<div onClick={onClick} style={{ border: '1px solid #ccc', borderRadius: '6px', padding: '16px', marginBottom: '12px', cursor: 'pointer', background: '#f9f9f9' }}>
			<h3 style={{ margin: 0, color: '#007bff', textDecoration: 'underline' }}>{task.title}</h3>
			<p style={{ margin: '4px 0' }}><strong>Subject:</strong> {task.subject}</p>
			<p style={{ margin: '4px 0' }}><strong>Status:</strong> {task.status}</p>
			<p style={{ margin: '4px 0' }}><strong>Priority:</strong> {task.priority}</p>
		</div>
	);
};

export default TaskItem;
