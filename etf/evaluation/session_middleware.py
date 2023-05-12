from datetime import timedelta, datetime

from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware


class MaxAgeSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        super().process_request(request)
        session = request.session
        max_age = getattr(settings, 'SESSION_MAX_AGE', 604800)  # 7 days in seconds
        session_created_at = session.get("session_created_at")
        if session_created_at is not None:
            created_at = datetime.strptime(session_created_at, '%Y-%m-%dT%H:%M:%S')
            age = datetime.now() - created_at
            if age > timedelta(seconds=max_age):
                session.flush()
        session['_session_expiry'] = datetime.now()
