 # Stage 1: Build the Spring Boot application (Maven or Gradle)
   FROM maven:3.8-jdk-11 AS build   
   WORKDIR /app
   COPY pom.xml .
   RUN mvn clean package  

   FROM openjdk:11-jre-slim  
   WORKDIR /app
   COPY --from=build /app/target/*.jar app.jar
   EXPOSE 8080
   ENTRYPOINT ["java", "-jar", "app.jar"]