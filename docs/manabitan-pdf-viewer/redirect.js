const destination = new URL('web/', window.location.href)
destination.search = window.location.search
destination.hash = window.location.hash
document.getElementById('viewer-link').href = destination.href
window.location.replace(destination.href)
