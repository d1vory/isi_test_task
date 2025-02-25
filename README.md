# Django Test Task

This is a test task.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Running

1. Clone this repository:

   ```sh
   git clone https://github.com/d1vory/isi_test_task
   cd isi_test_task
   ```
2. Create **.env** file from **.env_example**

    ```sh
   cp .env_example .env
   ```

3. Start the project using Docker Compose:

   ```sh
   docker-compose up
   ```

4. Access the application:

   - API documentation (Swagger): [http://localhost:8000/swagger](http://localhost:8000/swagger)
   - Django app: [http://localhost:8000](http://localhost:8000)


### Admin Credentials

- Username: `d1vory`
- Password: `testpass123`

### User Credentials

- Every account has the same password: `testpass123`


### Stopping the Project

To stop the running containers, use:

```sh
docker-compose down
```

### Environment Variables

Ensure you have a `.env` file with the necessary environment variables provided in .env_example

### Notes

- Make sure ports `8000` are not occupied before running the project.
