import sender_stand_request
import data

# Esta función cambia los valores en el parámetro "firstName"

def get_user_body(first_name):

    current_body = data.user_body.copy()    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body["firstName"] = first_name  # Se cambia el valor del parámetro firstName
    return current_body                     # Se devuelve un nuevo diccionario con el valor firstName requerido

def positive_assert(first_name):

    user_body = get_user_body(first_name)                           # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_response = sender_stand_request.post_new_user(user_body)   # El resultado de la solicitud relevante se guarda en la variable "user_response"

    assert user_response.status_code == 201                         # Comprueba si el código de estado es 201
    assert user_response.json()["authToken"] != ""                  # Comprueba que el campo authToken está en la respuesta y contiene un valor

    users_table_response = sender_stand_request.get_users_table()   # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]   # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así

    assert users_table_response.text.count(str_user) == 1           # Comprueba si el usuario existe y es único

    print(f'\nDatos del usuario enviados: \n\t{user_body}')
    print(f'\nStatus_code = {user_response.status_code}')
    print(f'json = {user_response.json()}')

def negative_assert_symbol(first_name):

    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == ('Has introducido un nombre de usuario no válido. '
                                               'El nombre solo puede contener letras del alfabeto latino, '
                                               'la longitud debe ser de 2 a 15 caracteres.') #Se pueden utilizar \ para salto de linea o encerrar todo entre parentesis.

    print(f'\nDatos del usuario enviados: \n\t{user_body}')
    print(f'\nStatus_code = {response.status_code}')
    print(f'json = {response.json()}')

def negative_assert_no_first_name(user_body):

    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == 'No se han aprobado todos los parámetros requeridos' #El mensaje indicado es diferente a la respuesta real: 'No se enviaron todos los parámetros necesarios'

    print(f'\nDatos del usuario enviados: \n\t{user_body}')
    print(f'\nStatus_code = {response.status_code}')
    print(f'json = {response.json()}')

def  test_create_user_2_letter_in_first_name_get_success_response():
    print('\n\tPRUEBA 1: Para un nombre de usuario de 2 caracteres "Aa":')
    positive_assert("Aa")

def  test_create_user_15_letter_in_first_name_get_success_response():
    print('\n\tPRUEBA 2: Para un nombre de usuario de 15 caracteres "Aaaaaaaaaaaaaaa":')
    positive_assert("Aaaaaaaaaaaaaaa")

def  test_create_user_1_letter_in_first_name_get_error_response():
    print('\n\tPRUEBA 3: Para un nombre de usuario de 1 caracter "A":')
    negative_assert_symbol("A")

def  test_create_user_16_letter_in_first_name_get_error_response():
    print('\n\tPRUEBA 4: Para un nombre de usuario de 16 caracteres "Aaaaaaaaaaaaaaaa":')
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

def  test_create_user_has_space_in_first_name_get_error_response():
    print('\n\tPRUEBA 5: Para un nombre de usuario que contiene espacios "A Aaa":')
    negative_assert_symbol("A Aaa")

def  test_create_user_has_special_symbol_in_first_name_get_error_response():
    print('\n\tPRUEBA 6: Para un nombre de usuario que contiene caracteres especiales "\"N°%@\",":')
    negative_assert_symbol("\"N°%@\",")

def  test_create_user_has_number_in_first_name_get_error_response():
    print('\n\tPRUEBA 7: Para un nombre de usuario que contiene numeros "123":')
    negative_assert_symbol("123")

def  test_create_user_no_first_name_get_error_response():
    print('\n\tPRUEBA 8: El nombre de usuario no se pasa en la solicitud:')
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

def  test_create_user_empty_first_name_get_error_response():
    print('\n\tPRUEBA 9: Para un nombre de usuario vacio:')
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)

def  test_create_user_number_type_first_name_get_error_response():
    print('\n\tPRUEBA 10: Para un nombre de usuario con datos tipo numerico:')
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400

    print(f'\nDatos del usuario enviados: \n\t{user_body}')
    print(f'\nStatus_code = {response.status_code}')
    print(f'json = {response.json()}')

test_create_user_2_letter_in_first_name_get_success_response()

test_create_user_15_letter_in_first_name_get_success_response()

test_create_user_1_letter_in_first_name_get_error_response()

test_create_user_16_letter_in_first_name_get_error_response()

#test_create_user_has_space_in_first_name_get_error_response()

test_create_user_has_special_symbol_in_first_name_get_error_response()

test_create_user_has_number_in_first_name_get_error_response()

test_create_user_no_first_name_get_error_response()

test_create_user_empty_first_name_get_error_response()

test_create_user_number_type_first_name_get_error_response()