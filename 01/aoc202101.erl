-module(aoc202101).
-export([start/0]).

start() ->
    {ok, File} = file:open("input.txt",[read]),
    Dlist = read_int(File, [], []),
    file:close(File).

read_int(File, A) ->
    Apa = io:fread(File, "", "~d"),
    case Apa of
    eof -> 
        A;
    {ok, [N]} ->
        read_int(File, [N | A]);
    {error, What} -> 
        io:format("io:fread error: ~w~n", [What]),
        A
    end.
