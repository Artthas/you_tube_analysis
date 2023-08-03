FROM node:18.17.0

ARG NEXT_PUBLIC_BACK_API_URL

ENV NEXT_PUBLIC_BACK_API_URL=$NEXT_PUBLIC_BACK_API_URL

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD [ "npm", "start" ]
