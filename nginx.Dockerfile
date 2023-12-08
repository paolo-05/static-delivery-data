# Use the official Nginx image
FROM nginx:alpine

# Remove the default configuration since we are using ours
RUN rm /etc/nginx/conf.d/default.conf

# Copy nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx/ssl /etc/nginx/ssl

# Expose the port Nginx will run on
EXPOSE 80 443

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
