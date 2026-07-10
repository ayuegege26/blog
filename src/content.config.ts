import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const archive = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/archive' }),
  schema: z.object({
    title: z.string(),
    type: z.enum([
      'essay',
      'research',
      'system',
      'signal',
      'project',
      'failure',
      'experiment',
      'journal',
      'unknown',
    ]),
    status: z.enum(['draft', 'active', 'stable', 'archived', 'ongoing', 'future']),
    summary: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    tags: z.array(z.string()),
    field: z.enum(['research', 'systems', 'signals', 'essays', 'projects', 'experiments']),
    featured: z.boolean().default(false),
    priority: z.number().default(999),
    slug: z.string().optional(),
    objectId: z.string().optional(),
    cover: z.string().optional(),
    related: z.array(z.string()).optional(),
    links: z
      .object({
        demo: z.string().url().optional().or(z.literal('')),
        repo: z.string().url().optional().or(z.literal('')),
        reference: z.string().url().optional().or(z.literal('')),
      })
      .optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { archive };
