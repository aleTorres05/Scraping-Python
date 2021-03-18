# Busacador de Códigos Postales

### Objetivo

Desarrollar un _web scrapper_ que sea capaz de **recopilar** la información de códigos postales de México de este [sitio](https://micodigopostal.org/).
Para posteriormente gguardarlo en un archivo json.

O de igual manera, utilizar la base de datos proporcionada por [Correos de México](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx) y extraer los datos de igual manera a un _json_.

### Justificación

Con el objeto de mejorar la experiencia de usuario de [jade](https://github.com/eldefiar/jade) y [coral](https://github.com/eldefiar/coral), y tener mejor presición a la hora de capturar datos, se utilizará el resultado (_json_) de éste programa para poder servirlo en el API de **jade**.

### Recomendaciones

Se recomienda utilizar el lenguaje de programación [Python](https://www.python.org/) y de las librerías:

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://2.python-requests.org/en/master/)
- [httpx](https://www.python-httpx.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [Librerías Estándar](https://docs.python.org/3.8/library/index.html)

### Notas

- Si no tiene ciudad, omitirla como _string_ vacío

### Especificación del JSON

    [
        {
            "municipio": "Municipio Ejemplo",
            "estado": "Estado Ejemplo",
            "ciudad: "Ciuad Ejemplo",
            "asentamiento": "Colonia Ejemplo",
            "tipo_asentamiento": "Colonia",
            "codigo_postal": "69420"
        },
        ...
    ]
