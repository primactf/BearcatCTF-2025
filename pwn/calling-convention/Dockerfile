FROM pwn.red/jail AS challenge_base
COPY --from=ubuntu /  /srv
RUN mkdir /srv/app/

FROM challenge_base AS challenge
ENV JAIL_PORT=5000
COPY calling_convention /srv/app/run
COPY flag.txt /srv/app/
