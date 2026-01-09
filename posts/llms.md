---
title: LLMs
date: 2025-12-12
author: Jack
excerpt: Part 4 of an introduction to AI - how neural networks become language generators
---

# LLMs

Now you understand the architecture. There is more we could get into. If you're curious about more details on the architecture side, the seminal paper worth your time is ["Attention is all you need"](https://arxiv.org/abs/1706.03762). I will warn you, it's complicated. 

Luckily we don't need it. You now understand a [perceptron](/blog/perceptron), you understand how language can be converted into [vectors](/blog/vectors), and you understand how a series of connected perceptrons forms a [neural network](/blog/neural_network). There have been advances in making those neural networks even more efficient, but we don't need to get into it. The big issue we left off with was how do we go from a classifier to a generator. 

## Training Tasks

Ignoring the math, the logic behind the answer is simple - a smart training task. Previous examples of training tasks we've discussed are positive vs. negative sentiment and junk vs. relevant news articles. BERT, the large language model I used for my thesis, used two training tasks - Masked Language Modelling and Next Sentence Prediction. Masked Language Modelling would take a sentence and randomly "mask" or hide words in the sentence, and then the task would be to predict the hidden word. Think about how simple that is. 

Example sentence:

	I am sitting in a cafe writing about AI.

Example task:
	
	I am ___ in a cafe writing about AI.

And now because we know the correct response, we can guess and check. The model will output a prediction for this task. First time let's say it tries "I am *coffee* in a cafe writing about AI". Wrong, let's adjust the weights and try again. Next attempt - "I am *sit* in a cafe writing about AI". Still wrong, but closer. We continue adjusting the weights until we get it correct - that is, until we get our output prediction to match our true masked word. And we aren't doing this one sentence at a time, we are doing it millions at a time, and adjusting weights until our cumulative scores look good. The training data is ample. All of Wikipedia, all of Reddit, the entire Library of Congress. And the task is easy. We know the right answers, so there's no need to label data. We can just iterate on word prediction until our model predicts them at higher and higher frequency. 

## Next Word Prediction

Now this isn't the task used by modern LLMs, but it's close enough. Modern LLMs found that just predicting the next word was a more straightforward and scalable training task. As you read this sentence, try to predict what word will come next before you read it. Are you doing it? Probably hard with all the words close together. I'll space them out in a stretch below, you can maybe cover your hand and scroll slowly.

This

Is

The 

Task

That

Created

Modern

Artificial

Intelligence.

How

Does

It

Feel?

That's the basis, that's how LLM's learn. They practice predicting the next word until they get really good at it. After that, they do a couple of "post-training" tasks. They build a model that understands natural language, then they "tune" it to take advantage of that language understanding. These training tasks look a lot more like our interactions with LLMs. Given a question, what's an ideal output? The data here is obviously much smaller, and much more difficult to generate and label, but once all the understanding is baked in, fewer examples are needed to direct the model towards specific behavior. 

## Reinforcement Learning via Human Feedback

I'll touch on one more interesting advancement responsible for a significant leap forward. I remember in my Master's learning about GPT 2 and 3 - they were impressive in their own right. But the big jump from 3 to ChatGPT (3.5) was made using something called RLHF. That stands for Reinforcement Learning via Human Feedback. It's a simple idea - humans generally have good instincts on judging outputs. We can read two texts and tell which one feels better, more useful, more human (This also happens to be the thesis of the [Turing Test](https://en.wikipedia.org/wiki/Turing_test)). OpenAI had their models produce pairs of outputs, and had humans decide which output felt better. They then fed that information back into the model, rewarding the weights that produced the better output. This is obviously expensive - you need humans actually reading and grading individual outputs, but this "reinforcement learning" turned out to make a huge difference, and is often credited as a major differentiator in the era of modern chatbots. 

## The Building Blocks

We've done it. We're at the end of the road. Our building blocks:

1. A large, flexible architecture that allows for learning nuance. 

2. An unimaginable amount of training data (and a smart way of making that training data machine readable).

3. Smart training tasks to take advantage of all that training data, with some clever fine-tuning to polish it off.

4. Iterations. Lots and lots and lots of iterations.

That's it. And now that I've explained all that, I can explain what it means going forward. 

-----
*Thanks for reading!*