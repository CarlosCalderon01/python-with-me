class Plugin:
    def ejecutar(self):
        print("plugin")

class EditorDeTexto:
    #variables para guardar los plugins
    def __init__(self):
        self.plugins = []
        print("crado variable")
        
    # metodo para guardar el "plugin" en var "plugins"
    def agregar_plugin(self, plugin):
        self.plugins.append(plugin)
        print("plugin agregado")

    def ejecutar_plugins(self):
        for plugin in self.plugins:
            plugin.ejecutar()

# creo var editor class EditorDeTexto
editor = EditorDeTexto()

# agrega los plugins en el almacen
editor.agregar_plugin(Plugin())
editor.agregar_plugin(Plugin())

# ejecutar para cada plugin almacenado
editor.ejecutar_plugins()

#instancio objetos y paso las clases a travez de sus propias funciones