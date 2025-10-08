// Utilidades para conversión de fechas entre formatos del backend y frontend
// Backend: YYYY-MM-DD (formato ISO)
// Frontend: YYYY-MM-DD (formato para inputs type="date")
// Display: DD/MM/YYYY (formato legible para mostrar al usuario)

/**
 * Convierte fecha del backend (YYYY-MM-DD) a formato para input type="date" (YYYY-MM-DD)
 * Los inputs type="date" requieren formato YYYY-MM-DD
 * @param {string} dateStr - Fecha en formato del backend
 * @returns {string} - Fecha en formato para input date
 */
export function backendToFrontendDate(dateStr) {
	if (!dateStr) return '';
	
	// Si es formato ISO completo (YYYY-MM-DDTHH:MM:SS)
	if (dateStr.includes('T')) {
		return dateStr.split('T')[0]; // Retorna solo la parte de la fecha YYYY-MM-DD
	}
	
	// Si es formato SQL (YYYY-MM-DD HH:MM:SS)
	const match = dateStr.match(/(\d{4})[/-](\d{2})[/-](\d{2})/);
	if (match) {
		const [, year, month, day] = match;
		return `${year}-${month}-${day}`;
	}
	
	return '';
}

/**
 * Convierte fecha del frontend (YYYY-MM-DD) a formato del backend (YYYY-MM-DD)
 * Los inputs type="date" ya devuelven formato YYYY-MM-DD, así que no necesita conversión
 * @param {string} dateStr - Fecha en formato del frontend (YYYY-MM-DD)
 * @returns {string} - Fecha en formato del backend (YYYY-MM-DD)
 */
export function frontendToBackendDate(dateStr) {
	if (!dateStr) return '';
	
	// Los inputs type="date" ya devuelven formato YYYY-MM-DD
	// Solo validamos que tenga el formato correcto
	const match = dateStr.match(/(\d{4})-(\d{2})-(\d{2})/);
	if (match) {
		return dateStr; // Ya está en el formato correcto
	}
	
	return '';
}

/**
 * Formatea una fecha para mostrar al usuario en formato legible
 * @param {string} dateStr - Fecha en cualquier formato
 * @returns {string} - Fecha formateada para mostrar
 */
export function formatDateForDisplay(dateStr) {
	if (!dateStr) return '';
	
	// Convertir a formato legible DD/MM/YYYY
	const backendDate = dateStr.includes('T') ? dateStr.split('T')[0] : dateStr;
	const match = backendDate.match(/(\d{4})[/-](\d{2})[/-](\d{2})/);
	if (match) {
		const [, year, month, day] = match;
		return `${day}/${month}/${year}`;
	}
	
	return dateStr;
}
