import React, { Component } from 'react';
import './App.css';


class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      productos: [],
      recuperado: false
    }
  }

  componentDidMount() {
    fetch('http://localhost:8000/api/producto')
      .then((response) => {
        return response.json()
      })
      .then((prod) => {
        this.setState({
          productos: prod,
          recuperado: true
        })
      })
  }

  mostrarTabla() {
    return (
      <div>
        <table border="1">
          <thead>
            <tr>
              <th>Código</th>
              <th>Descripción</th>
              <th>Precio</th>
            </tr>
          </thead>
          <tbody>
            {this.state.productos.map(producto => {
              return (
                <tr key={producto.id}>
                  <td>{producto.id}</td>
                  <td>{producto.nombre}</td>
                  <td>{producto.precio}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  }
  render() {
    if (this.state.recuperado)
      return this.mostrarTabla()
    else
      return (<div>recuperando datos...</div>)
  }

}

export default App
