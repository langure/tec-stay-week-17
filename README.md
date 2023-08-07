# Week 17: Text Summarization: Abstractive and Extractive Approaches
Text summarization is a subfield of Natural Language Processing (NLP) focused on creating a concise summary of a longer text while maintaining its key information and overall meaning. This can be particularly useful for quickly understanding the content of large documents or aggregating information from multiple sources. There are two main approaches to text summarization: abstractive and extractive.

Extractive Summarization
Extractive summarization involves identifying the important sections of the text and generating the summary by directly extracting these sections from the source text. These sections could be sentences, phrases, or paragraphs. The key challenge in extractive summarization is to determine which parts of the text are most informative and relevant to the summary.

For example, consider the following text:

"The cat sat on the mat. It was a sunny day and the cat seemed very comfortable."

An extractive summarization of this could be:

"The cat sat on the mat. The cat seemed very comfortable."

Here, the second sentence is taken directly from the source text without any modifications.

Abstractive Summarization
Abstractive summarization, on the other hand, involves generating new sentences to express the important information in the source text. It doesn't just extract the key sentences, but rather paraphrases and condenses the information. This requires a deeper understanding of the text, and the ability to express this understanding in new words.

Continuing with the previous example, an abstractive summary might look like this:

"The cat was comfortably sitting on the mat enjoying the sunny day."

Notice that this sentence doesn't directly appear in the source text, but is a condensed and paraphrased version of the original information.

Choosing Between Abstractive and Extractive
The choice between abstractive and extractive summarization typically depends on the specific requirements of the task at hand. Extractive summarization can be useful when you want to ensure the summary contains only information present in the source text, but it might lead to summaries that lack cohesion or contain redundant information.

On the other hand, abstractive summarization can produce more fluent and coherent summaries, and can condense information more effectively. However, it is generally more challenging as it requires sophisticated language generation capabilities and there's a risk of introducing information not present in the source text.

Various algorithms and techniques exist for both types of summarization, including rule-based methods, machine learning techniques, and more recently, deep learning models like sequence-to-sequence architectures and transformer models, such as BERT and GPT, which have shown promising results especially in abstractive summarization.

# Readings

[Review of automatic text summarization techniques & methods](https://pdf.sciencedirectassets.com/280416/1-s2.0-S1319157822X00049/1-s2.0-S1319157820303712/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIDHmUoFBGXNTWhXvIOIk%2F%2F9D%2FzSPYDDUY7xJ7lzfU6keAiBDoMibAde2MBsXyEhtlWC77cDC1RycC1jxZGDd1BLEzCqyBQh5EAUaDDA1OTAwMzU0Njg2NSIMUoPDtqwtDbkKtKrGKo8FJtZvvXDS%2BXQqWsLki%2FnkFQUD9N37bDdY1S0NyxeO9n1ZZhAWc3Gs2fHstgugG6mj%2FTu6hKjHzvpaoUf3%2FbTYtVwvB62IABQvNcLhv3MaZPCPXQPiBtUFvkI64LZjNledOg%2FRntPvU5Fhc%2BWielwco%2Bfcd0NEVPbi2qqZp3Bb4RbG212RcQVQTZLMhs1kcwKYK7tUYowhZKWvl45O5%2Fcq7ayCCNaG00nLaak3ilq%2FxmLmrh2tMzeGz6hgn%2FWQ6rSwo3i6s61WrXktWr%2Bmn%2BNq8gltHJRYjX7dRL2%2BPFCO9elN5IWxgsMM7TkAZjErAAWtoDE54lOD%2Bqg%2FeFFLzHNiVMT3DSgnHsDerCGeMBuylZTTYKbVcAA1GZTHKsTQK4pUSLkZAulfAYaucyJnHrnuNsC5mgEOdd46mfpJtgUUJU7Aqt5GgTqlGYWhRim6aCOtqRnqyvP0PN%2B%2FTsEliTTWHVA%2BdjIM7sNkbiUV4CmMsA8yxYwyOjplu%2FfMzISibnCSRqdhN8za0%2FsS0NRZ5ccMPLeS7512e8W%2BrHjlT4WvDHQSm5k6hGmfL6cu4xMfcW0UkTo6eudVHLEM%2F4eTrslO8AFRJVCwcVgaZcsb61qRfj2FUlBCtJvkM4y2Rlu908nJTzKUUj7nRTHILz2bsCbX%2FDB0vkL9QIXeCYh5bIQmt%2Fo7wxt4%2FgWaHv6BatDYx1s1yBxlnwyOL1pBG%2BeoSXqr%2F%2FwLH8LAx6%2BgA9H4eKT9e%2FIV9Rlg5IQmGJl0pGt0ljFLiYcQG6%2B0%2F62urYoBI8uZcpHfzOTH9apIDipgwuqLlYyYDXEqtpvxqAY1OJ1yPPM41Nnd1QazgAmPh2Lu565mEzAPSbQAGsvFMBzivZA69zCapcSmBjqyAe9HhVHuTEAfZKXMuB4RqT2NMTO4HEQtPq%2BfQ5v6achG7fecTnmacHc7sR7MXS7mAy4KzAesm5KIdGagMPqGPRuqXfyJB%2BIgaBgn836UXs1hLaThLwrakl8Bp0FEhAvoOazFn343unEH6JztQpkfDwrIUxy2x5GnDW0Q7yAjv57N2PSoNcOVWtGGVulC%2BiJCNMKCBZmH4vHCWvMBM3Ser3kFxeg2%2FZWAYa5t8LLF4fVGJbI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230807T162409Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXDTMNSXJ%2F20230807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=37915629a02e987d7811efd7a52e9bec6ed630cd2ff9df6d3697baf96fc797c1&hash=6478f0660288433adf11ecf4b37fb0b740cfb48dbc7f42b40ed3e4456ff2bb10&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1319157820303712&tid=spdf-c14d8f9d-6acb-4790-9055-94c201ebc105&sid=3f710ca98816f94e725bb7119f6d8cbf3c6agxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1719550651530300575b&rr=7f30de446ff71549&cc=mx)


[Review of automatic text summarization techniques & methods](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=c4f3ab8f0f9e370b37f0ac154999074169d3aa3e#page=104)


# Code example
