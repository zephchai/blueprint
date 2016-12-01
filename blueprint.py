import os
import json
'''
def getPathsToCreate(template):
    """ Read the template and call traversePath to get the list of paths to
        create

        Args:
            template: path to the root of the template

        Return:
            (list): List of path to create
    """
    paths = traversePath(template)
    if not template.endswith(os.sep):
        template = template + os.sep
    
    # Remove the template folder from the paths
    paths = [path.replace(template, "") for path in paths]

    return sorted(paths)
'''

def getPathsToCreate(path, realPath="", pathsToCreate=[]):
    """ Traverse the given path and return the paths to create.
        If there are more folders in the path, it will traverse recursively.

        Args:
            path: path to traverse

        Return:
            (list): List of paths to create
        
    """

    items = sorted(os.listdir(path))
    if "config.json" in items:
        # This is a keyword directory level
        configFile = os.path.join(path, "config.json")
        with open(configFile, "r") as f:
            config = json.load(f)
            
        env = config["env"]
        envValue = os.getenv(env)
        
        if not envValue:
            # Something may be wrong here but we will just skip this folder
            return pathsToCreate
        # At this point, there are 2 possibilities here.
        # Case1: envValue is in items. Follow that directory.
        # Case2: envValue is not in items. Follow the directory that is same
        # name as env.

        if envValue in items:
            newPath = os.path.join(path, envValue)
            newRealPath = os.path.join(realPath, envValue)

        else:
            newPath = os.path.join(path, env)
            newRealPath = os.path.join(realPath, envValue)
        
        pathsToCreate.append(newRealPath)
        getPathsToCreate(newPath, newRealPath, pathsToCreate)

    else:
        # This is a normal directory level
        for item in items:
            newPath = os.path.join(path, item)
            newRealPath = os.path.join(realPath, item)
            pathsToCreate.append(newRealPath)
            getPathsToCreate(newPath, newRealPath, pathsToCreate)

    return pathsToCreate
