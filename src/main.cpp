#include <fmt/core.h>
#define SDL_MAIN_HANDLED
#include <SDL2/SDL.h>

#include "simple_mod.hpp"

int main(int,char**) {

    print_hello_world();

    int init_flags = SDL_INIT_TIMER | SDL_INIT_VIDEO;
    if (SDL_Init(init_flags) != 0) {
        fmt::println(stderr, "SDL failed to init: {}", SDL_GetError());
        return EXIT_FAILURE;
    }

    int window_flags = SDL_WINDOW_SHOWN;
    SDL_Window *window = SDL_CreateWindow("Hello World!",
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
            800, 600, window_flags);
    if (window == nullptr) {
        fmt::println(stderr, "SDL failed to create window: {}", SDL_GetError());
        return EXIT_FAILURE;
    }

    bool running = true;
    while (running)
    {
        SDL_Event event;
        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
            case SDL_QUIT:
                running = false;
                break;
            
            default:
                break;
            }
        }
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return EXIT_SUCCESS;
}