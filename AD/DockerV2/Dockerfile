   # Use the official Maven image as the base image
   FROM maven:3.6.3-jdk-11-slim AS build

   # Set the working directory in Docker

   # Copy the pom.xml and the src code to the container
   COPY . .

   # Package the application
   RUN mvn -f /pom.xml clean package

   # Use the official OpenJDK image as the base image for the runner
   FROM openjdk:11-jre-slim

   # Copy the jar from the build stage
   COPY --from=build /target/your-springboot-app.jar /usr/local/lib/app.jar

   # Specify the entry point
   ENTRYPOINT ["java","-jar","/usr/local/lib/app.jar"]