import ee
import datetime
import geemap

# Autenticação
try:
    ee.Initialize(project = 'teste-476811')
except Exception as e:
    ee.Authenticate()
    ee.Initialize(project = 'teste-476811')

# Conversão de data do objeto ee do servidor para o cliente
ee_date = ee.Date('2023-01-08')
py_date = datetime.datetime.fromtimestamp(ee_date.getInfo()['value']/1000, datetime.UTC)

# Conversão de data do cliente para o objeto ee do servidor 
py_date = datetime.datetime.now(datetime.UTC)
ee_date = ee.Date(py_date)

# Exportação de dados
# task = ee.batch.Export.image.toDrive(image=my_image,  # an ee.Image object.
#                                      region=my_geometry,  # an ee.Geometry object.
#                                      description='mock_export',
#                                      folder='gdrive_folder',
#                                      fileNamePrefix='mock_export',
#                                      scale=1000,
#                                      crs='EPSG:4326')
# #task.start()
#task.status()

# Obtenção de imagens serializadas 

img = ee.ImageCollection("Spain/PNOA/PNOA10")

# Recomendado o uso de libs externas complementares como geemap, Folium, ipyleaflet

# Inicializar um objeto mapa

img = ee.Image.random()
Map = geemap.Map()
Map.addLayer(img, None, "Random")
Map
