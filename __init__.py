import cuiViewer
import cuiBuilder

BUILDER_INSTANCE = None
VIEWER_INSTANCE = None

def builder():
  global BUILDER_INSTANCE
  reload(cuiBuilder)
  BUILDER_INSTANCE = cuiBuilder.CUIBuilder()
  BUILDER_INSTANCE.show()

def viewer():
  global VIEWER_INSTANCE
  reload(cuiViewer)
  VIEWER_INSTANCE = cuiViewer.CUIViewer()
  VIEWER_INSTANCE.show()

def killCUI():
  global BUILDER_INSTANCE, VIEWER_INSTANCE

  if BUILDER_INSTANCE:
    BUILDER_INSTANCE.close()
    BUILDER_INSTANCE.deleteLater()
    BUILDER_INSTANCE = None

  if VIEWER_INSTANCE:
    VIEWER_INSTANCE.close()
    VIEWER_INSTANCE.deleteLater()
    VIEWER_INSTANCE = None

def update():
  killCUI()
  import update
  update.updateFromGitHub()
  