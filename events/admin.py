# from django.contrib import admin

# # Register your models here.
# import graphene

# class Query(graphene.ObjectType):
#   hello = graphene.String(name=graphene.String(default_value="World"))

#   def resolve_hello(self, info, name):
#     return 'Hello ' + name

# schema = graphene.Schema(query=Query)
# result = schema.execute('{ hello }')
# print(result.data['hello']) # "Hello World"


# import graphene

# class Query(graphene.ObjectType):
#     hello = graphene.String(argument=graphene.String(default_value="stranger"))
    
#     def resolve_hello(self, info,argument):
#         return 'World'+argument


# schema = graphene.Schema(query=Query)

# data=schema.execute('{hello (argument: "graph")}')
# print(data.data['hello'])