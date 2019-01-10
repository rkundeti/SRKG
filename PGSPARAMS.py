import yaml
with open("C:\Ramana_Python\DBCONFIG.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    index = 'pgsql'
    PGHOST=cfg[index]['host']
    PGUSER = cfg[index]['user']
    PGPASSWORD = cfg[index]['passwd']
    PGPORT = cfg[index]['port']
    PGDATABASE = cfg[index]['db']






