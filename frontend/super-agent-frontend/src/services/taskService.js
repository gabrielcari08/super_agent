import api from './api';

// This service handles API requests related to tasks.
// Este servicio maneja las peticiones API relacionadas con tareas.

export const taskService = {
  // Get all tasks for the authenticated user
  // Obtener todas las tareas del usuario autenticado
  getTasks: async () => {
    const response = await api.get('/tasks/get_tasks');
    return response.data;
  },
  // Delete a task by ID
  // Eliminar una tarea por ID
  deleteTask: async (taskId) => {
    const response = await api.delete(`/tasks/delete_task/${taskId}`);
    return response.data;
  },
  // Update a task by ID
  // Actualizar una tarea por ID
  updateTask: async (taskId, taskData) => {
    const response = await api.put(`/tasks/update_task/${taskId}`, taskData);
    return response.data;
  },
};
