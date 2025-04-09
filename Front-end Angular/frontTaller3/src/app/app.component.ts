import { Component } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [CommonModule,HttpClientModule, FormsModule]
})
export class AppComponent {
  // Variables para el formulario de inserción
  nombre = '';
  matricula = '';
  hora = '';
  fecha = '';

  // URL de la API para insertar registro y para obtener registros
  private apiUrlInsert = 'http://localhost:5000/insert_record';
  private apiUrlGet = 'http://localhost:5000/get_records';

  // Array para guardar los registros obtenidos de la base de datos
  records: any[] = [];

  constructor(private http: HttpClient) {}

  // Método para enviar datos al endpoint de inserción
  onSolicitar() {
    const formData: FormData = new FormData();
    formData.append('nombre', this.nombre);
    formData.append('matricula', this.matricula);
    formData.append('hora', this.hora);
    formData.append('fecha', this.fecha);

    this.http.post(this.apiUrlInsert, formData).subscribe(
      (response: any) => {
        console.log('Registro insertado:', response);
        alert("Formulario enviado con éxito");
      },
      (error: any) => {
        console.error('Error al insertar:', error);
        alert("No se pudo enviar el formulario");
      }
    );
  }

  // Método para obtener todos los registros de la base de datos
  onGetRecords() {
    this.http.get(this.apiUrlGet).subscribe(
      (response: any) => {
        console.log('Registros obtenidos:', response);
        this.records = response;
      },
      (error: any) => {
        console.error('Error al obtener registros:', error);
        alert("No se pudo obtener los registros");
      }
    );
  }
}
