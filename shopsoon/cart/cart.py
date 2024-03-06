class Cart():

    def __init__(self, request):
        self.session = request.session

        # Returnning user after obtaining his session key
        cart = self.session.get('session_key')

        if 'session_key' not in request.session: # If the user has not logged in
            cart = self.session['session_key'] = {}
        
        self.cart = cart