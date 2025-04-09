import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [HttpClientModule, FormsModule]
})
export class AppComponent {
  nombre = '';
  matricula = '';
  hora = '';
  fecha = '';

  private apiUrl = 'http://localhost:5000/insert_record';

  constructor(private http: HttpClient) {}

  onSolicitar() {
    const formData: FormData = new FormData();
    formData.append('nombre', this.nombre);
    formData.append('matricula', this.matricula);
    formData.append('hora', this.hora);
    formData.append('fecha', this.fecha);

    this.http.post(this.apiUrl, formData).subscribe(
      (response: any) => {
        console.log('Registro insertado:', response);
        // Aquí puedes agregar lógica adicional, como limpiar el formulario o mostrar una notificación.
      },
      (error: any) => {
        console.error('Error al insertar:', error);
      }
    );
  }
}
