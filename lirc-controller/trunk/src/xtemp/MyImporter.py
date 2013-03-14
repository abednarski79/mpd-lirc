class Loader:
    
    def __init__(self):
        self.modulesCache = {}
        self.classesCache = {}
        self.methodsCache = {}            
        
    def findModuleByName(self, moduleName):
        module = None
        if(self.modulesCache.has_key(moduleName)):
            module = self.modulesCache[moduleName]
        if(module == None):
            module = __import__(moduleName)
            self.modulesCache[moduleName] = module
        return module
    
    def findClassInstanceByName(self, moduleName, className):
        classInstance = None        
        cacheKey = moduleName + "." + className
        if(self.classesCache.has_key(cacheKey)):
            classInstance = self.classesCache[cacheKey]        
        if(classInstance == None):
            module = self.findModuleByName(moduleName)
            clazz = getattr(module, className)
            classInstance = clazz()
            self.classesCache[cacheKey] = classInstance
        return classInstance
    
    def findMethodInstanceByName(self, moduleName, className, methodName):
        methodInstance = None
        cacheKey = moduleName + "." + className + "." + methodName            
        if(self.methodsCache.has_key(cacheKey)):
            methodInstance = self.methodsCache[cacheKey]
        if(methodInstance == None):
            classInstance = self.findClassInstanceByName(moduleName, className)
            methodInstance = getattr(classInstance, methodName)
            self.methodsCache[cacheKey] = methodInstance
        return methodInstance
    
def main():
    loader = Loader()
    method1 = loader.findMethodInstanceByName("MyModule", "MyClass", "myMethod")
    method2 = loader.findMethodInstanceByName("MyModule", "MyClass", "myMethod")
    print method1
    method1()
    print method2
    method2()

main()