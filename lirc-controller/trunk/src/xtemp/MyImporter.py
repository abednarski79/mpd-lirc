class Loader:
    
    def __init__(self):
        self.modulesCache = {}
        self.classesCache = {}
        self.methodsCache = {}            
        
    def findModuleByName(self, moduleName):
        module = self.modulesCache[moduleName]
        if(module == None):
            module = __import__(moduleName)
            self.modulesCache[moduleName] = module
        return module
    
    def findClassInstanceByName(self, moduleName, className):        
        classInstance = self.classesCache[moduleName + "." + className]
        if(classInstance == None):
            module = self.findModuleByName(moduleName)
            clazz = getattr(module, className)
            classInstance = clazz()
            self.classesCache[moduleName + "." + className] = classInstance
        return classInstance
    
    def findMethodInstanceByName(self, moduleName, className, methodName):
        cacheKey = moduleName + "." + className + "." + methodName            
        if(self.methodsCache.has_key(cacheKey)):
            methodInstance = self.methodsCache[cacheKey]
        if(methodInstance == None):
            classInstance = self.classesCache[moduleName + "." + className]
            methodInstance = getattr(classInstance, methodName)
            self.methodsCache[cacheKey] = methodInstance
def main():
    loader = Loader()
    method1 = loader.findMethodInstanceByName("MyModule", "MyClass", "myMethod")
    method2 = loader.findMethodInstanceByName("MyModule", "MyClass", "myMethod")
    print method1
    print method2

main()