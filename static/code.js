const carrito = document.querySelector('#carrito');
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.querySelector('#vaciar-carrito');
const listaProductos = document.querySelector('#lista-productos');
let articulosCarrito = [];

// Crear eventos
cargarEventos();
function cargarEventos() {
	// Agregar curso
	listaProductos.addEventListener('click', agregarProducto);
	// Eliminar curso del carrito
	contenedorCarrito.addEventListener('click', eliminarProducto);
	// Varciar cursos del carrito
	vaciarCarritoBtn.addEventListener('click', () => {
		articulosCarrito = [];
		limpiarHTML();
	});
}

// Agregar curso
function agregarProducto(e) {
	e.preventDefault();
	if (e.target.classList.contains('agregar-carrito')) {
		const productoSeleccionado = e.target.parentElement.parentElement;
		leerProducto(productoSeleccionado);
	}
}

// Eliminar curso del carrito
function eliminarProducto(e) {
	if (e.target.classList.contains('borrar-producto')) {
		const productoID = e.target.getAttribute('data-id');

		// Eliminar del array del carrito
		articulosCarrito = articulosCarrito.filter((producto) => producto.id !== productoID);
		carritoHTML();
	}
}

// Leer curso seleccionado
function leerProducto(producto) {
	const infoProducto = {
		img: producto.querySelector('img').src,
		titulo: producto.querySelector('h4').textContent,
		precio: producto.querySelector('.precio').textContent,
		id: producto.querySelector('a').getAttribute('data-id'),
		cantidad: 1
	};

	const existe = articulosCarrito.some((producto) => producto.id === infoProducto.id);

	if (existe) {
		// actualizar la cantidad
		const productos = articulosCarrito.map((producto) => {
			// Con map creamos nuevo array
			if (producto.id === infoProducto.id) {
				producto.cantidad++;
				return producto;
			} else {
				return producto;
			}
		});
		articulosCarrito = [ ...productos ];
	} else {
		articulosCarrito = [ ...articulosCarrito, infoProducto ];
	}
	carritoHTML();
}

// Mostrar en conetenedor HTML
function carritoHTML() {
	limpiarHTML();

	// Recorrer array
	articulosCarrito.forEach((producto) => {
		const row = document.createElement('tr');
		row.innerHTML = `
		<td>
			<img src="${producto.img}" width="100">
		</td>
		<td> ${producto.titulo} </td>
		<td> ${producto.precio} </td>
		<td> ${producto.cantidad} </td>
		<td>
			<a href="#" class="borrar-producto" data-id="${producto.id}">X</a>
		</td>
		`;

		// Mostrar en HTML
		contenedorCarrito.appendChild(row);
	});
}

// Limpiar HTML
function limpiarHTML() {
	while (contenedorCarrito.firstChild) {
		contenedorCarrito.removeChild(contenedorCarrito.firstChild);
	}
}
