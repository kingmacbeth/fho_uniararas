Requirements:

1) Docker
2) Python 3.6+

Run the following command to start Keycloak server:

docker run -p 8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:26.0.6 start-dev

Configure your Keycloak client and google identity provider.

Check if credentials are correct in the python files then run the server.
