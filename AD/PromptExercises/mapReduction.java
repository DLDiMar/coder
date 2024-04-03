import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    @Override
    protected void setup(Context context) throws IOException, InterruptedException {
        // Initialization tasks for the mapper (if needed)
    }

    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        // Split the line into words
        String[] words = value.toString().split("\\s+");

        // Emit (word, 1) for each word
        for (String word : words) {
            context.write(new Text(word), new IntWritable(1));
        }
    }

    @Override
    protected void cleanup(Context context) throws IOException, InterruptedException {
        // Finalization tasks for the mapper (if needed)
    }
}
