# Aegis Platform Overview

## Introduction
Aegis is a cutting-edge platform built using CrewAI, designed as a Generative AI (GenAI) tool to produce a comprehensive set of high-quality blogs based on any given topic. Leveraging Large Language Models (LLMs), Aegis streamlines the blog creation process from research to publication. Its goal is to deliver credible, structured, and visually appealing blog articles while minimizing manual effort.

## Core Functionality
Aegis integrates a multi-agent system to handle the entire lifecycle of blog creation. The platform is built on collaborative agents, each with a specific responsibility, ensuring seamless workflow and high-quality output. By automating research, content generation, technical enhancement, formatting, and publication, Aegis transforms raw ideas into professional, publish-ready blogs.

## Key Features
- **Comprehensive Research:** Aegis ensures all blog content is rooted in credible and up-to-date information, leveraging advanced data-gathering techniques.
- **Structured Content Creation:** The platform generates logically organized articles with well-defined sections, summaries, and takeaways for intuitive readability.
- **Enriched Content:** Each blog is expanded with in-depth details, ensuring depth and clarity while maintaining factual accuracy.
- **Code Integration:** Aegis includes technical code snippets in multiple programming languages (e.g., Python, Java) for blogs requiring technical examples, enhancing reader comprehension.
- **Smooth Content Flow:** The platform reviews and refines the logical transitions between sections, creating a cohesive and engaging narrative.
- **SEO and HTML Formatting:** Blogs are formatted in HTML, designed for readability and optimized for search engines. The platform also ensures visual appeal with the use of structured tags like `<h3>` and highlights.
- **Automated Publishing:** Aegis handles the seamless publishing of blogs to WordPress via API integration, ensuring accuracy and consistency.

## Workflow Summary
1. **Research and Planning:** Aegis begins by uncovering reliable information on the chosen topic and structuring it into a clear outline.
2. **Content Development:** Detailed content is created and enriched, supplemented with technical examples where applicable.
3. **Review and Enhancement:** The generated content undergoes review to ensure logical flow and clarity.
4. **Formatting and Publishing:** The final article is formatted in HTML, optimized for SEO, and published directly to WordPress.

## Benefits of Aegis
- **Efficiency:** Automates multiple stages of blog creation, reducing time and effort.
- **Credibility:** Ensures content is based on verified and reliable sources.
- **Technical Accuracy:** Enhances technical blogs with practical, well-documented code examples.
- **Professional Presentation:** Produces visually appealing, SEO-friendly articles ready for publication.
- **Seamless Integration:** Direct publishing to WordPress with robust API handling.

## Conclusion
Aegis represents a breakthrough in automated content creation, providing an all-in-one solution for generating and publishing professional blogs. By combining research, writing, technical expertise, and publishing in one platform, Aegis simplifies the blogging process and sets a new standard for AI-driven content generation.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/aegis/config/agents.yaml` to define your agents
- Modify `src/aegis/config/tasks.yaml` to define your tasks
- Modify `src/aegis/crew.py` to add your own logic, tools and specific args
- Modify `src/aegis/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Aegis Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Aegis Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.