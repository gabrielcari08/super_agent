// This page is responsible for displaying the list of tasks for the authenticated user, with filters and access to task details.
// Esta página se encarga de mostrar la lista de tareas del usuario autenticado, con filtros y acceso al detalle de cada tarea.

import React, { useState, useEffect } from 'react';
import TaskList from '../components/TaskList';
import { taskService } from '../services/taskService';
import { TASK_TYPES, TASK_PRIORITIES, TASK_STATUSES, SUBJECT_TYPES } from '../constants/taskEnums';
import { backendToFrontendDate, frontendToBackendDate, formatDateForDisplay } from '../utils/dateUtils';

// The TaskListPage component will render the list of tasks and filtering options.
// El componente TaskListPage renderizará la lista de tareas y las opciones de filtrado.


const TaskListPage = () => {
	// State for edit mode and edit form data
	const [editMode, setEditMode] = useState(false);
	const [editTaskData, setEditTaskData] = useState({
		title: '',
		description: '',
		subject: '',
		task_type: '',
		status: '',
		priority: '',
		date_of_task: '',
		date_of_presentation: ''
	});
	// State for tasks
	// Estado para las tareas
	const [tasks, setTasks] = useState([]);

	// State for filters
	// Estado para los filtros
	const [filters, setFilters] = useState({
		subject: '',
		status: '',
		task_type: ''
	});

		// Fetch tasks from backend
		// Obtener tareas del backend
		useEffect(() => {
			const fetchTasks = async () => {
				try {
					const data = await taskService.getTasks();
					setTasks(data);
				} catch (error) {
					// You can show an error message here
					setTasks([]);
				}
			};
			fetchTasks();
		}, []);

	// Handler for filter changes
	// Manejador para cambios en los filtros
	const handleFilterChange = (e) => {
		setFilters({
			...filters,
			[e.target.name]: e.target.value
		});
	};

		// State for selected task (for detail view)
		// Estado para la tarea seleccionada (para vista de detalle)
		const [selectedTask, setSelectedTask] = useState(null);

		// Handler for clicking a task
		// Manejador para hacer click en una tarea
		const handleTaskClick = (task) => {
			setSelectedTask(task);
		};

		// Handler to close detail modal
		// Manejador para cerrar el modal de detalle
		const handleCloseDetail = () => {
			setSelectedTask(null);
		};

			// Use enum arrays for filters
			// Usar arrays de enums para los filtros
			const subjects = SUBJECT_TYPES;
			const statuses = TASK_STATUSES;
			const types = TASK_TYPES;

		// Filter tasks based on filters
		// Filtrar tareas según los filtros
		const filteredTasks = tasks.filter(task => {
			return (
				(filters.subject === '' || task.subject === filters.subject) &&
				(filters.status === '' || task.status === filters.status) &&
				(filters.task_type === '' || task.task_type === filters.task_type)
			);
		});

		return (
			<div style={{ padding: '40px' }}>
				<h2>Task List</h2>
				<TaskList
					tasks={filteredTasks}
					onTaskClick={handleTaskClick}
					filters={filters}
					onFilterChange={handleFilterChange}
					subjects={subjects}
					statuses={statuses}
					types={types}
				/>

				{/* Task detail modal */}
				{/* Modal de detalle de tarea */}
				{selectedTask && (
					<div style={{
						position: 'fixed',
						top: 0,
						left: 0,
						width: '100vw',
						height: '100vh',
						background: 'rgba(0,0,0,0.4)',
						display: 'flex',
						alignItems: 'center',
						justifyContent: 'center',
						zIndex: 1000
					}}>
						<div style={{ background: 'white', padding: '32px', borderRadius: '8px', minWidth: '350px', maxWidth: '90vw' }}>
							<h2>{selectedTask.title}</h2>
							<p><strong>Subject:</strong> {selectedTask.subject}</p>
							<p><strong>Type:</strong> {selectedTask.task_type}</p>
							<p><strong>Description:</strong> {selectedTask.description}</p>
							<p><strong>Date of Task:</strong> {formatDateForDisplay(selectedTask.date_of_task)}</p>
							<p><strong>Date of Presentation:</strong> {formatDateForDisplay(selectedTask.date_of_presentation)}</p>
							<p><strong>Status:</strong> {selectedTask.status}</p>
							<p><strong>Priority:</strong> {selectedTask.priority}</p>
							
							{editMode ? (
								<form
									onSubmit={async (e) => {
										e.preventDefault();
										// Convertir fechas del formato frontend (DD-MM-YYYY) al formato backend (YYYY-MM-DD)
										const dataToSend = {
											...editTaskData,
											date_of_task: editTaskData.date_of_task ? frontendToBackendDate(editTaskData.date_of_task) : null,
											date_of_presentation: editTaskData.date_of_presentation ? frontendToBackendDate(editTaskData.date_of_presentation) : null,
										};
										try {
											await taskService.updateTask(selectedTask.id, dataToSend);
											setTasks(tasks.map(t => t.id === selectedTask.id ? { ...t, ...editTaskData } : t));
											setEditMode(false);
											handleCloseDetail();
										} catch (error) {
											alert('Error updating task.');
										}
									}}
									style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '24px' }}
								>
									<input
										type="text"
										value={editTaskData.title}
										onChange={e => setEditTaskData({ ...editTaskData, title: e.target.value })}
										placeholder="Title"
										required
									/>
									<textarea
										value={editTaskData.description}
										onChange={e => setEditTaskData({ ...editTaskData, description: e.target.value })}
										placeholder="Description"
										required
									/>
									<select
										value={editTaskData.subject}
										onChange={e => setEditTaskData({ ...editTaskData, subject: e.target.value })}
										required
									>
										<option value="">Select Subject</option>
										{subjects.map(s => <option key={s} value={s}>{s}</option>)}
									</select>
									<select
										value={editTaskData.task_type}
										onChange={e => setEditTaskData({ ...editTaskData, task_type: e.target.value })}
										required
									>
										<option value="">Select Type</option>
										{types.map(t => <option key={t} value={t}>{t}</option>)}
									</select>
									<select
										value={editTaskData.status}
										onChange={e => setEditTaskData({ ...editTaskData, status: e.target.value })}
										required
									>
										<option value="">Select Status</option>
										{statuses.map(s => <option key={s} value={s}>{s}</option>)}
									</select>
									<select
										value={editTaskData.priority}
										onChange={e => setEditTaskData({ ...editTaskData, priority: e.target.value })}
										required
									>
										<option value="">Select Priority</option>
										{TASK_PRIORITIES.map(p => <option key={p} value={p}>{p}</option>)}
									</select>
									<input
										type="date"
										value={backendToFrontendDate(editTaskData.date_of_task)}
										onChange={e => setEditTaskData({ ...editTaskData, date_of_task: e.target.value })}
										required
									/>
									<input
										type="date"
										value={backendToFrontendDate(editTaskData.date_of_presentation)}
										onChange={e => setEditTaskData({ ...editTaskData, date_of_presentation: e.target.value })}
										required
									/>
									<div style={{ display: 'flex', gap: '12px', marginTop: '8px' }}>
										<button type="submit" style={{ padding: '10px 20px', background: '#28a745', color: 'white', border: 'none', borderRadius: '4px' }}>Save</button>
										<button type="button" onClick={() => setEditMode(false)} style={{ padding: '10px 20px', background: '#6c757d', color: 'white', border: 'none', borderRadius: '4px' }}>Cancel</button>
									</div>
								</form>
							) : (
								<div style={{ marginTop: '24px', display: 'flex', gap: '16px' }}>
									<button onClick={() => {
										setEditTaskData({
											title: selectedTask.title,
											description: selectedTask.description,
											subject: selectedTask.subject,
											task_type: selectedTask.task_type,
											status: selectedTask.status,
											priority: selectedTask.priority,
											date_of_task: backendToFrontendDate(selectedTask.date_of_task),
											date_of_presentation: backendToFrontendDate(selectedTask.date_of_presentation)
										});
										setEditMode(true);
									}} style={{ padding: '10px 20px', background: '#ffc107', color: '#333', border: 'none', borderRadius: '4px' }}>Edit</button>
									<button
										onClick={async () => {
										if (window.confirm('Are you sure you want to delete this task?')) {
											try {
												await taskService.deleteTask(selectedTask.id);
												setTasks(tasks.filter(t => t.id !== selectedTask.id));
												handleCloseDetail();
											} catch (error) {
												alert('Error deleting task.');
											}
										}
									}}
									style={{ padding: '10px 20px', background: '#dc3545', color: 'white', border: 'none', borderRadius: '4px' }}
									>Delete</button>
									<button onClick={handleCloseDetail} style={{ padding: '10px 20px', background: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}>Close</button>
								</div>
							)}
						</div>
					</div>
				)}
			</div>
		);
};

export default TaskListPage;