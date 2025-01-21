<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> 📈 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations

### Infrastructure Component Considerations

In this section we will provide a brief introduction of key components of the infrastructure.

1. **Docker**:

- We are using docker in our infra as a docker runtime and also we are transforming our code into a Docker image, and when we need to set up the Central Hub deployment, we simply download the latest image and run 
  a Docker container with it to deploy the entire infrastructure.
- We used docker as a runtime in our infrastructure because of it's ease of use, also it's provides a complete set of tools for container management, including Docker compose we can manage the multicontainer 
  applications within a single configuration file. Additionally, Docker has ability to create multistage Dockerfiles which helps us to build light weight Docker images by seperating the build environment from the 
  runtime environment. This reduce the image size and improves the performance.

