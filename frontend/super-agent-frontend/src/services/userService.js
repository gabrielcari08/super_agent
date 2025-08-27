import api from './api';

export const userService = {
  createUser: async (userData) => {
    try {
      const response = await api.post('/users/create_user', userData);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Error al crear usuario');
    }
  }
};