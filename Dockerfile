FROM golang:1.15
MAINTAINER "jesse.ha" <jesse.ha@kakaocorp.com>

COPY ./elevator /go/src/2019-blind-2nd-elevator/elevator
COPY ./dataset /go/src/2019-blind-2nd-elevator/dataset

WORKDIR /go/src/2019-blind-2nd-elevator/elevator
RUN go mod init 2019-blind-2nd-elevator/elevator

WORKDIR /go/src/2019-blind-2nd-elevator/elevator/cmd/elevator
RUN mkdir -p /go/src/2019-blind-2nd-elevator/logs
RUN go build

EXPOSE 8000
CMD ./elevator
